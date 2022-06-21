const { Client, Intents, MessageEmbed } = require("discord.js")

 

const client = new Client({

    intents: [

      Intents.FLAGS.GUILDS,

      Intents.FLAGS.GUILD_MESSAGES

    ]

})

 

client.on("ready", () => {

    console.log("機器人已經成功上線且載入成功!")

})

 

client.on("messageCreate", (message) => {

    const prefix = "!" // 如果要改成自己的前綴，改"裡面的字串

    if (!message.content.startsWith(prefix))

        return

    

    const args = message.content.slice(prefix.length).split(" ")

    switch (args[0]) {

        case "dice":

            const final = Math.floor(Math.random() * (6 - 1)) + 1

            const diceEmbed = new MessageEmbed()

                .setTitle(`🎲 你得到了 ${final}`)

                .setColor("#5865F2")

            return message.reply({

                embeds: [diceEmbed]

            })

    }

})

    

client.login("OTY4NDc3OTA5MTg0NTQ0Nzk4.GirQpQ.jwJI-ZERRlT1S68ghUVqU-8tK6uSA7gTSc7cQ8")