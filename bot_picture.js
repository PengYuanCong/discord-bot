const {Client} = require('discord.js') ;
const client = new Client ;
const settings = require('./setting.json') ;

client.on("ready",()=>{

    console.log("機器人已經成功上線且載入成功!")

})

client.on("messageCreate", (message) => {

    const prefix = "!" // 這個是機器人的前綴 (aka 開頭 aka 觸發符號)

    if (!message.content.startsWith(prefix))

        return

})

client.on('message',msg=>{ 
    if(msg.content.startsWith(settings.prefix+'pic')){
        var rnd = Random(7,1) ;
        msg.channel.send({files:["./picture/"+num+".png"]});
    }

    if(msg.content.startsWith(settings.prefix='PIC')){
        var rnd = Random(7,1) ;
        switch(rnd){
            case 1 : msg.channel.send({files:["./picture/1.png"]}) ;break;
            case 2 : msg.channel.send({files:["./picture/2.png"]}) ;break;
            case 3 : msg.channel.send({files:["./picture/3.png"]}) ;break;
            case 4 : msg.channel.send({files:["./picture/4.png"]}) ;break;
            case 5 : msg.channel.send({files:["./picture/5.png"]}) ;break;
            case 6 : msg.channel.send({files:["./picture/6.png"]}) ;break;
            case 7 : msg.channel.send({files:["./picture/7.png"]}) ;break;
        }
    }
function Random(max,min){
    var rnd = Math.floor(Math.random()*max)+min ;
    return rnd ;
}

});

client.login("OTY4NDc3OTA5MTg0NTQ0Nzk4.GirQpQ.jwJI-ZERRlT1S68ghUVqU-8tK6uSA7gTSc7cQ8") ;