const nodemailer = require('nodemailer');

function sendReceiptEmail(name, email, fundSelection, donationAmount) {
    let transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: 'your-email@gmail.com',
            pass: 'your-email-password',
        },
    });

    const mailOptions = {
        from: 'your-email@gmail.com',
        to: email,
        subject: 'Donation Receipt - RGUKT Nuzvid',
        html: `
      <p>Dear ${name},</p>
      <p>Thank you for your donation!</p>
      <p><strong>Donation Receipt Details:</strong></p>
      <ul>
        <li><strong>Name:</strong> ${name}</li>
        <li><strong>Email:</strong> ${email}</li>
        <li><strong>Fund Selected:</strong> ${fundSelection}</li>
        <li><strong>Donation Amount:</strong> $${donationAmount}</li>
        <li><strong>Institution:</strong> RGUKT Nuzvid</li>
      </ul>
      <p>Thank you for supporting us!</p>
    `,
    };

    transporter.sendMail(mailOptions, function (error, info) {
        if (error) {
            console.log(error);
        } else {
            console.log('Email sent: ' + info.response);
        }
    });
}
