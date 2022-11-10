const request =  require("request");
let TDKEY = "4bfdf729a2ec4118b4ac1673f739b3da";
const prompt = require("prompt-sync")();

async function RealTimePrices(tickers) { 

    return await new Promise((resolve, reject) => {
        
    let tdurl = 'https://api.twelvedata.com/price?symbol=' +tickers.toString() + '&apikey=' + TDKEY;

    request.get({
        url: tdurl,
        json: true,
        headers: {'User-Agent': 'request'}
    }, (err, res, data) => {
        if (err) {
        console.log('Error:', err);
        } else if (res.statusCode !== 200) {
        console.log('Status:', res.statusCode);
        } else {
 
        let reformattedData = {};

        if(tickers.length == 1)
        {
            let key = tickers[0];
            reformattedData[key] = parseFloat(data.price);
        }
        else if(tickers.length > 1)
        { 
            for(let key in data)
            {
                reformattedData[key] = parseFloat(data[key].price);
            }
        }

        resolve(reformattedData);
    }
});



    });  


}

let tickername = prompt("Enter the ticker of the stock you would like to see in real time:");
let captickername = tickername.toUpperCase();

async function RepeatFunction()
{
    let search = await RealTimePrices([captickername]);

    console.log(search[captickername]);

}

    setInterval(RepeatFunction, 1000);


