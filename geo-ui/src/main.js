document.querySelector('#app').innerHTML = `
  <div style="padding:20px;">
    <h2>Mini GEO Audit Demo</h2>
    <input id="urlInput" placeholder="Enter URL" style="width:300px; margin-right:10px;" />
    <button id="auditBtn">Audit</button>
    <pre id="output"></pre>
  </div>
`;

document.getElementById("auditBtn").addEventListener("click", async () => {
  const url = document.getElementById("urlInput").value;

  const response = await fetch("http://127.0.0.1:8000/audit", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ url })
  });

  const data = await response.json();

  document.getElementById("output").textContent =
    JSON.stringify(data, null, 2);
});