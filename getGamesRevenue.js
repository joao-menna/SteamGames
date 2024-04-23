import { readFile, writeFile } from "fs/promises"
import puppeteer from "puppeteer"

(async () => {
    const contents = await readFile('./games.json')
    const games = JSON.parse(contents)

    // We have to treat it because it comes with a strange structure
    const gamesArray = []
    for (const key of Object.keys(games)) {
        gamesArray.push(games[key])
    }

    const browser = await puppeteer.launch({
        headless: false
    })
    const page = await browser.newPage()

    await page.goto('https://steam-revenue-calculator.com/')
    await page.setViewport({ width: 1920, height: 1080 })
    
    const gamesRevenue = []
    for (const game of gamesArray) {
        const totalReviews = game.positive + game.negative
        const price = parseInt(game.price) / 100

        const numberReviewsValue = await page.$eval('#number-of-reviews', (el) => el.value)
        const priceValue = await page.$eval('#price', (el) => el.value)

        await page.click('#number-of-reviews')
        for (let i = 0; i < numberReviewsValue.length; i++) {
            await page.keyboard.press('Backspace')
        }

        await page.click('#price')
        for (let i = 0; i < priceValue.length; i++) {
            await page.keyboard.press('Backspace')
        }

        await page.type('#number-of-reviews', totalReviews.toString())
        await page.type('#price', price.toString())

        const regionalPricing = await (await page.$('[data-testid="adjusted-regional-pricing"]')).evaluate((val) => val.innerText)
        const discounts = await (await page.$('[data-testid="discounts"]')).evaluate((val) => val.innerText)
        const refunds = await (await page.$('[data-testid="refunds"]')).evaluate((val) => val.innerText)
        const steamCut = await (await page.$('[data-testid="steam-fee"]')).evaluate((val) => val.innerText)
        const tax = await (await page.$('[data-testid="vat"]')).evaluate((val) => val.innerText)
        const netRevenue = await (await page.$('[data-testid="net-revenue"]')).evaluate((val) => val.innerText)

        gamesRevenue.push({
            appid: game.appid,
            name: game.name,
            developer: game.developer,
            publisher: game.publisher,
            totalReviews,
            price: price,
            regionalPricing: parseFloat(regionalPricing.replace('$', '').replaceAll(',', '')),
            discounts: parseFloat(discounts.replace('$', '').replaceAll(',', '')),
            refunds: parseFloat(refunds.replace('$', '').replaceAll(',', '')),
            steamCut: parseFloat(steamCut.replace('$', '').replaceAll(',', '')),
            tax: parseFloat(tax.replace('$', '').replaceAll(',', '')),
            netRevenue: parseFloat(netRevenue.replace('$', '').replaceAll(',', ''))
        })
    }

    await writeFile('./games_with_revenue.json', JSON.stringify(gamesRevenue, undefined, 2))

    await browser.close()
})()