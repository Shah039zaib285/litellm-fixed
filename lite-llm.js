const axios = require('axios');
const endpoint = process.env.LITELLM_ENDPOINT;
async function generateReply(message) {
    const response = await axios.post(endpoint, {
        model: "gpt-4o-mini",
        messages: [{role:"user", content: message}],
        max_tokens: 250
    });
    return response.data.choices[0].message.content;
}
module.exports = { generateReply };