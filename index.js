const { cloud, login_cellphone } = require('NeteaseCloudMusicApi')
const fs = require('fs')
const path = require('path')

async function main() {
  const result = await login_cellphone({
    phone: process.env.PHONE,
    password: process.env.PASSWORD,
  }).catch(e => console.error(e))
  const filePath = fs.readFileSync('song_name.txt').toString()
  try {
    const resp = await cloud({
      songFile: {
        name: path.basename(filePath),
        data: fs.readFileSync(filePath),
      },
      cookie: result.body.cookie,
    })
    console.log(resp)
  } catch (error) {
    console.log(error, 'error')
  }
}
await main().catch(e => console.error(e))