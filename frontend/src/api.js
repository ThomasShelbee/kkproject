let api_host = import.meta.env.VITE_BACKEND_URL

async function getItems() {
    let items = await fetch(`${api_host}/api/get-items`)
    return await items.json()
}

async function getPromos() {
    let promos = await fetch(`${api_host}/api/get-promos`)
    return await promos.json()
}

async function getGif() {
    let gif = await fetch(`${api_host}/api/get-gif`)
    return await gif.json()
}

async function deletePromoBack(promo) {
    promo = await fetch(`${api_host}/api/delete-promo/${promo.id}`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(promo)
    })
    return await promo.json()
}

async function sendPurchase(newPurchase) {
    let purchase = await fetch(`${api_host}/api/purchase`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(newPurchase)
    })
    return await purchase.json()
}

export {getItems, getPromos, deletePromoBack, getGif, sendPurchase, api_host}