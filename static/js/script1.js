function fetchData() {
    fetch('/get_data')
        .then(response => {
            if (!response.ok) {
                throw new Error('An error occurred while fetching data.');
            }
            return response.json();
        })
        .then(data => {
            displayData(data);
        })
        .catch(error => {
            console.error('Error:', error);
            // Display error message on the HTML page
            document.getElementById('data-display').innerHTML = 'An error occurred while fetching data.';
        });
}

function displayData(data) {
    const tableBody = document.getElementById('data-body');
    // Clear previous data
    tableBody.innerHTML = '';

    // Iterate over the data and create table rows
    data.forEach(row => {
        const tr = document.createElement('tr');
        Object.values(row).forEach(value => {
            const td = document.createElement('td');
            td.textContent = value;
            tr.appendChild(td);
        });
        tableBody.appendChild(tr);
    });
}

// Call fetchData when the page loads
window.onload = fetchData;
