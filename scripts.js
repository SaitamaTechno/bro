function read_file(file){
  var text
  function readTextFile(file) {
      var rawFile = new XMLHttpRequest();
      rawFile.open("GET", file, false);
      rawFile.onreadystatechange = function () {
        if(rawFile.readyState === 4)  {
          if(rawFile.status === 200 || rawFile.status == 0) {
            var allText = rawFile.responseText;
            text=allText
            //console.log(allText);
          }
        }
      }
      rawFile.send(null);
    }
    readTextFile(file)
    text= JSON.parse(text)
    const js = JSON.parse(text)
    return js
}
    //document.getElementById("myPlot").style.width=window.innerWidth
    document.getElementById("myPlot").style.minHeight = (window.innerHeight-200).toString()+"px"
    
    console.log(window.innerHeight, window.innerWidth)
    //const xArray = [50,60,70,80,90,100,110,120,130,140,150];
    //const yArray = [7,8,8,9,9,9,10,11,14,14,15];
    //console.log(js)
    const dls=read_file("DLS.json")
    const dly=read_file("DLY.json")
    const fark_list=[]
    for(var i=0; i<dls.close.length; i++){
      fark=dly.close[i]-dls.close[i]
      fark_list.push(fark)
    }
    
    const xArray = dls.date;
    const yArray = fark_list;
    var mylen=dls.date;
    // Define Data
    const data = [{
      x: xArray,
      y: yArray,
      mode:"scatter"
    }];
    
    // Define Layout
    const layout = {
      xaxis: {range: mylen, title: "Dates"},
      yaxis: {range: mylen, title: "DLY - DLS"},  
      title: "DLY - DLS Fark Grafiği",
      paper_bgcolor: "lightblue", //background color of the chart container space
      plot_bgcolor: "lightyellow", //background color of plot area
    };
    
    // Display using Plotly
    Plotly.newPlot("myPlot", data, layout, {scrollZoom: true});
  