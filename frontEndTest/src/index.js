import { saveAs } from 'file-saver';

window.addEventListener("load", () => {
    console.log("loaded");
    const uploadInput = document.getElementById("fileUploader");
    const uploadBtn = document.getElementById("uploadBtn");
    const downloadBtn = document.getElementById("downloadBtn");

    let selectedFile;
    let downloadedFile;

    uploadInput.onchange = (e) => {
        const fileList = e.target.files || [];
        console.log(fileList);
        selectedFile = fileList[0];
    };

    uploadBtn.addEventListener('click', () => {
        const data = new FormData();
        data.append("file", selectedFile);
        data.append("name", selectedFile.name);
        data.append("type", selectedFile.type);
    
        (async () => {
            const res = await fetch(
                "http://localhost:5000/api/v1/products/file",
                {
                    method: "POST",
                    body: data,
                }
            );
            const resFormdata = await res.formData();
            downloadedFile = resFormdata.get('file');
        })();
    });

    downloadBtn.addEventListener('click', () => saveAs(downloadedFile, downloadedFile.name));
});
