const qs = (el) => document.querySelector(el)
const qsAll = (el) => document.querySelectorAll(el)

//player info
const $playerName = qs('.p-name')
const $playerBalance = qs('.p-balance')

// game
const $btnBet = qs('.btn-bet')
const $coinBg = qs('.coin-background')
const $imgCoin = qs('.coin-animation')


$btnBet.addEventListener('pointerdown', (ev) => {
    $imgCoin.classList.add('on')
    $coinBg.classList.add('on')
    setTimeout(() => {
        $imgCoin.classList.remove('on')
        $coinBg.classList.remove('on')
        runGame($btnBet.getAttribute('data-game-id'))
    }, 2000)
})

const getPlayerInfo = async () => {
    const response = await fetch('/player-info')
    const data = await response.json()
    $playerName.innerText = data.username
    updateBalance(data)
}

const runGame = async (game_id) => {
    const response = await fetch(`/game/${game_id}/run`)
    const data = await response.json()
    if (data.error) {
        alert(data.error)
        return;
    }
    updateBalance(data)
}

const updateBalance = (data) => {
    $playerBalance.innerText = data.balance
}

getPlayerInfo()