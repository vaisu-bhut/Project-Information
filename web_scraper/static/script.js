async function startScraping() {
    const url = document.getElementById('urlInput').value;
    const outputDiv = document.getElementById('output');
    const statusDiv = document.getElementById('status');
    const spinner = document.getElementById('spinner');
    const pageCountDiv = document.getElementById('pageCount');

    if (!url) {
        statusDiv.textContent = "Please enter a valid URL";
        statusDiv.style.color = "#ff5555";
        return;
    }

    statusDiv.textContent = "AI is analyzing...";
    statusDiv.style.color = "#ffd700";
    spinner.style.display = "block";
    outputDiv.innerHTML = "";
    pageCountDiv.textContent = "Pages Scraped: 0";
    let totalPages = 0;

    // Connect to WebSocket
    const ws = new WebSocket(`ws://localhost:8000/ws/scrape?url=${encodeURIComponent(url)}`);

    ws.onmessage = (event) => {
        const data = JSON.parse(event.data);
        const batchSize = Object.keys(data).length;
        totalPages += batchSize;
        outputDiv.innerHTML += JSON.stringify(data, null, 2) + "\n\n";
        statusDiv.textContent = `AI is processing more pages... (Batch: ${batchSize})`;
        pageCountDiv.textContent = `Pages Scraped: ${totalPages} - Level Up!`;
    };

    ws.onerror = (error) => {
        statusDiv.textContent = "Error occurred during scraping";
        statusDiv.style.color = "#ff5555";
        spinner.style.display = "none";
        outputDiv.innerHTML += "Error: " + error.message + "\n";
    };

    ws.onclose = () => {
        statusDiv.textContent = "Scraping complete!";
        statusDiv.style.color = "#00ff00";
        spinner.style.display = "none";
        pageCountDiv.textContent = `Mission Accomplished! Total Pages Scraped: ${totalPages}`;
    };
}