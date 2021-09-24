var colorIndex = 0
var colorList = ["#4d4d4d", "#00A19D", "#E05D5D", "#FFB344"]
function doimau() {
    if (colorIndex >= 3) {
        colorIndex = -1
    }
    colorIndex += 1
    var nextColor = colorList[colorIndex]
    document.getElementById("p1").style.color = nextColor
    document.getElementById("p2").style.color = nextColor
    document.getElementById("p3").style.color = nextColor
}

var bgColorIndex = 0
var bgColorList = ["#FFF", "#00B8A9", "#F6416C", "#FFDE7D"]

function doiMauNen() {
    if (bgColorIndex >= 3) {
        bgColorIndex = -1
    }
    bgColorIndex += 1
    var nextColor = bgColorList[bgColorIndex]
    document.getElementById("header").style.backgroundColor = nextColor
}

function doiNoiDung(p1,p2,type) {
    if (type == 'id') {
        var p1Content = document.getElementById(p1).innerText
        var p2Content = document.getElementById(p2).innerText
        document.getElementById(p1).innerText = p2Content
        document.getElementById(p2).innerText = p1Content
    }else{
        var p1Content = document.getElementsByClassName('para')[p1].innerText
        var p2Content = document.getElementsByClassName('para')[p2].innerText
        document.getElementsByClassName('para')[p1].innerText = p2Content
        document.getElementsByClassName('para')[p2].innerText = p1Content
    }
}

var allSizeChanged  = false
function doiKichThuocTatCa(newSize) {
    var baseSize = 12
    if (allSizeChanged) {
        newSize = baseSize
    }
    var listP = document.getElementsByClassName('para')
    for (let i = 0; i < listP.length; i++) {
        const element = listP[i];
        element.style.fontSize = newSize+"px"
    }
    allSizeChanged = !allSizeChanged
}

function tangKichThuoc(index) {
    var el = document.getElementsByClassName('para')[index]
    var style = window.getComputedStyle(el).getPropertyValue('font-size');
    var fontSize = parseFloat(style);
    if (fontSize<30) {
        el.style.fontSize = (fontSize + 1) + 'px';    
    }
}

function giamKichThuoc(index) {
    var el = document.getElementsByClassName('para')[index]
    var style = window.getComputedStyle(el).getPropertyValue('font-size');
    var fontSize = parseFloat(style); 
    if (fontSize>10) {
        el.style.fontSize = (fontSize - 1) + 'px';    
    }
}