document.getElementById("donationForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent form submission

    // Get form data
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const fundSelection = document.getElementById("fundSelection").value;
    const donationAmount = document.getElementById("donationAmount").value;

    // Display receipt message and download button
    document.getElementById("receiptMessage").style.display = "block";
    // Update receipt content
    document.getElementById("receiptName").textContent = name;
    document.getElementById("receiptEmail").textContent = email;
    document.getElementById("receiptFund").textContent = fundSelection;
    document.getElementById("receiptAmount").textContent = `$${donationAmount}`;

    // Send receipt via email (server-side logic needed here)
    sendReceiptEmail(name, email, fundSelection, donationAmount);

    // Set up the download button to generate the receipt PDF
    document.getElementById("downloadReceiptBtn").addEventListener("click", function () {
        downloadReceiptPDF(name, email, fundSelection, donationAmount);
    });
});

function sendReceiptEmail(name, email, fundSelection, donationAmount) {
    // Use server-side logic (e.g., Node.js, PHP, etc.) to send the email with the receipt.
    // This is just a placeholder to show where the email would be sent.
    console.log(`Sending receipt to ${email}...`);
    // In a real setup, you would use an email API (like SendGrid, Mailgun, etc.) to send the email.
}

function downloadReceiptPDF(name, email, fundSelection, donationAmount) {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    // Set up the receipt content
    doc.setFontSize(16);
    doc.text("Donation Receipt", 20, 20);

    doc.setFontSize(12);
    doc.text(`Name: ${name}`, 20, 40);
    doc.text(`Email: ${email}`, 20, 50);
    doc.text(`Fund Selected: ${fundSelection}`, 20, 60);
    doc.text(`Donation Amount: $${donationAmount}`, 20, 70);
    doc.text(`Institution: RGUKT Nuzvid`, 20, 80);

    // Customize donation amount text color to red and underline it
    doc.setTextColor(255, 0, 0); // Red color
    doc.text(`Donation Amount: $${donationAmount}`, 20, 70);
    doc.setTextColor(0, 0, 0); // Reset color back to black

    // Save the PDF
    doc.save('donation_receipt.pdf');
}
