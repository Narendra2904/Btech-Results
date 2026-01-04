import twilio from "twilio";

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ ok: false, error: "Method not allowed" });
  }

  const { name, email, roll, feedback } = req.body;

  const client = twilio(process.env.TWILIO_SID, process.env.TWILIO_TOKEN);

  const textMessage = `
📩 New Feedback
👤 Name: ${name}
📧 Email: ${email}
🎓 Roll: ${roll}
💬 ${feedback}
  `;

  try {
    await client.messages.create({
      from: "whatsapp:+14155238886",  
      to: `whatsapp:+91${process.env.MY_NUMBER}`,
      body: textMessage
    });
    res.status(200).json({ ok: true });
  } catch (err) {
    console.error("TWILIO SEND ERROR:", err);
    res.status(500).json({ ok: false });
  }
}
