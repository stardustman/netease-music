const { cloud,login_cellphone } = require('NeteaseCloudMusicApi')
const fs = require('fs')
const path = require('path')

async function main() {
  const result = await login_cellphone({
    phone: process.env.PHONE,
    password: process.env.PASSWORD,
  })
  const filePath = fs.readFileSync('song_name.txt').toString()
  try {
    await cloud({
      songFile: {
        name: path.basename(filePath),
        data: fs.readFileSync(filePath),
      },
      cookie: result.body.cookie,
    })
  } catch (error) {
    console.log(error, 'error')
  }
}
main()