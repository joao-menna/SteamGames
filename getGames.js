// Runs only in Node 18+

import fs from 'fs'

async function getGamesFromSteamSpy() {
    /**
     * Gets one page of steamspy
     * @param {number} page Page
     * @returns Apps
     */
    async function getSteamApps(page) {
        // tries to reach steamspy api
        try {
            const apps = await fetch(`https://steamspy.com/api.php?request=all&page=${page}`)
            return apps
        } catch (err) {
            console.error(`SteamSpy page ${page} not reached with the following error: ${err}`)
            return false
        }
    }

    // steamspy api has total of 60 pages
    const pages = 60
    const reviewMinimum = 5000
    const appsObject = {}

    for (let i = 0; i <= pages; i++) {
        // cycles through all pages
        console.log(`Reading page ${i}...`)
        const promise = await getSteamApps(i)

        if (!promise) continue

        const json = await promise.json()

        for (const key in json) {
            // cycles through each steam app in this page
            const app = json[key]
            const reviews = app.positive + app.negative

            // adds app to appsObject if this app has over 5k reviews
            if (reviews > reviewMinimum) appsObject[key] = app
        }

        // sleep function (60s)
        // steamspy has a limit of 1 request per minute for the "all" requests
        await new Promise((resolve) => setTimeout(resolve, 60000))
    }

    const stringJson = JSON.stringify(appsObject, undefined, 2)

    try {
        // writes json file
        await fs.promises.writeFile('./games.json', stringJson)

        const appsLength = Object.keys(appsObject).length
        console.log(`JSON successfully created with ${appsLength} games.`)
    } catch (err) {
        return console.error(`Error while writing JSON file: ${err}`)
    }
}

getGamesFromSteamSpy()