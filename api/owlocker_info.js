const axios = require('axios');

module.exports = async (req, res) => {
  try {
    const response = await axios.get('https://owlocker.com/api/info', { timeout: 10000 });
    res.status(200).json(response.data);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
};