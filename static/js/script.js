let selectedBoxId = 'box1'; // Initially selected box

// Function to highlight the selected box
function highlightBox(selectedBox) {
    const boxes = document.querySelectorAll('.box');
    boxes.forEach(box => {
        box.classList.remove('selected');
    });
    selectedBox.classList.add('selected');
}

// Function to show results for the selected box
function showResults(boxId) {
    // Deselect previously selected box
    const previousSelectedBox = document.getElementById(selectedBoxId);
    previousSelectedBox.classList.remove('selected');

    // Highlight the selected box
    const selectedBox = document.getElementById(boxId);
    highlightBox(selectedBox);

    // Update selectedBoxId
    selectedBoxId = boxId;

    // Perform query based on the selected box
    // Here you can make AJAX calls to your server to fetch data from the database
    // For demonstration purposes, let's log the box number
    console.log(`Results for ${boxId}: Querying database...`);
}
