// Tested on Firefox!

setTimeout(() => {
    var captchaImageElement = document.getElementById("c_status_ctl00_contentplaceholder1_defaultcaptcha_CaptchaImage")
    var captchaInputElement = document.getElementById("Captcha")
    var submitElement = document.getElementById("ctl00_ContentPlaceHolder1_btnSubmit")
    
    function downloadBase64AsFile(base64, fileName) {
        var link = document.createElement("a");
        link.setAttribute("href", base64);
        link.setAttribute("download", fileName);
        link.click();
        link.remove()
    }
    
    function inputHandler(){
        captchaInputElement.removeEventListener("dblclick", inputHandler)
        downloadBase64AsFile(base64String, captchaInputElement.value.toUpperCase() + ".png")
    }
    
    var c = document.createElement("canvas");
    c.height = captchaImageElement.naturalHeight;
    c.width = captchaImageElement.naturalWidth;
    var ctx = c.getContext("2d");
    ctx.drawImage(captchaImageElement, 0, 0, c.width, c.height);
    var base64String = c.toDataURL();
    
    captchaInputElement.addEventListener("dblclick", inputHandler)
}, 2500)
