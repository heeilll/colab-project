fetch('data.json') // Colab에서 다운로드한 JSON 파일
    .then(response => response.json())
    .then(data => {
        document.body.innerHTML += `<pre>${JSON.stringify(data, null, 2)}</pre>`;
    });
