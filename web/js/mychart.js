

// 2) CSVから２次元配列に変換する関数
function csv2Array(str) {
  // csvData をリストとして定義
  var csvData = [];
  // strを\nで区切り、linesに代入
  var lines = str.split("\n");
  // linesの長さだけfor分で繰り返す
  for (var i = 0; i < lines.length; ++i) {
    // linesを,で区切り、1要素ずつcellsに代入
    var cells = lines[i].split(",");
    // csvDataのさいごにcellsの要素を一つずつ追加
    csvData.push(cells);
  }
  // csv2Arrayの戻り値としてcsvDataを返す
  return csvData;
}

function drawBarChart(data) {
  // tmpLabels tmpData1 tmoData2をそれぞれcsvの1列2列3列ようの配列として用意
  var tmpLabels = [], tmpData1 = [], tmpData2 = [];
  
// row が　data　のかずだけ繰り返しますよ
  for (var row in data) {
    tmpLabels.push(data[row][0])
    tmpData1.push(data[row][1])
    tmpData2.push(data[row][2])
  };

  // ctxにmyChartの機能を持たせる
  var ctx = document.getElementById("myChart");
  // ctxの設定が
  var myChart = new Chart(ctx, {
    // 線グラフ
    type: 'line',
    // データの属性
    data: {
      // 横軸のラベル
      labels: tmpLabels,
      datasets: [
        { label: "歪み", data: tmpData1, borderColor: "rgb(179,128,255)" },
        { label: "応力", data: tmpData2, borderColor: "rgb(153,255,85)" }
      ]
    }
  });

}
// main関数の定義。　mychart.jsが呼ばれたらこれが実行される
function mainChart() {
    console.log("you get it!!");

  // XMLHttpRequest はページ遷移をせずに非同期的にサーバーと通信するajaxの基幹技術
  // XMLHttpRequest(ajax通信)をreqで縮小。javascriptを少し勉強すればいつもやる方法とわかるはず
  var req = new XMLHttpRequest();
  //fileの場所をfilepathに代入。相対パス
  var filePath = 'data.csv';
  console.log(filePath);
  // open() means initialize request. Asynchronouse connection == true
  req.open("GET", filePath, true);

  // このページと対象csvファイルが一通りloadをされたのちに
  req.onload = function() {
    // csv2Arrayにreqに格納した情報を渡す。　そしてその返り値をdataに代入
    data = csv2Array(req.responseText);
    // drawBarChartにdataを渡す。
    drawBarChart(data);
  }
  // GETメソッドの時の最後に描く
  req.send(null);
}
