const form = document.getElementById('comment') // Получение формы.
let
    player = document.getElementById('player_id').textContent ? document.getElementById('player_id').textContent : false,
    comment_text = false

// Событие submit формы.
form.addEventListener('submit', event => {
    event.preventDefault()
    comment_text = document.getElementById('id_comment_text').value ? document.getElementById('id_comment_text').value : false
    if (comment_text && player) {
        let data = {}
        data.player = Number(player)
        data.comment_text = comment_text
        send_comment(data) // Функция передачи данных на сервер.
    }
})

// Функция передачи данных на сервер.
const send_comment = async data => {
    try {
        // Определение данных для передачи на червер через axios.
        const url = '/api/comments/'
        axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
        axios.defaults.xsrfCookieName = 'csrftoken'
        let response = await axios.post(url, data)

        // Выполнение условия при положительном ответе от сервера.
        if (response.status === 201) {
            let success = document.getElementById('responseSRV')
            document.getElementById('id_comment_text').value = ''
            success.textContent = 'Коментарий успешно добавлен'
            success.classList.add('text-success')

            get_comments() // Функция плучения комментариев от сервера.

        }
    } catch (e) {
        // Выполнение условия при отрицательном ответе от сервера.
        let error = document.getElementById('responseSRV')
        error.textContent = 'Произошла не предвиденная ошибка, комментарий не был добавлен'
        error.classList.add('text-danger')
    }
}

// Функция плучения комментариев от сервера.
const get_comments = async () => {
    let comments = document.getElementById('comments'),
        comments_build = '',
        comment
    comments.textContent = 'Коментарии отсутствуют'

    try {
        // Определение данных для передачи на червер через axios.
        const url = `/api/comments/?player=${Number(player)}&ordering=-publication_date`
        axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
        axios.defaults.xsrfCookieName = 'csrftoken'
        let response = await axios.get(url)

        if (response.status === 200) {
            // Выполнение условия при положительном ответе от сервера, построение комментарии.
            response.data.forEach(function (obj) {
                comment = `<div>${obj.comment_text}</div>
                               <div><small><i>${get_date(obj.publication_date)}</i></small></div>
                               <hr/>`
                comments_build += comment
            })
            if (comments_build){
                comments.innerHTML = comments_build
            }
        }
    } catch (e) {
        console.log(e.response)

    }
}

get_comments()

// Вспомогательные функции, функции для правильного отображения даты.
function get_date(date) {
    date = new Date(date)
    let day = date.getDate(),
        month = date.getMonth(),
        year = date.getFullYear(),
        hours = addZero(date.getHours()),
        minutes = addZero(date.getMinutes())
    return `${year}-${month}-${day} ${hours}:${minutes}`
}

function addZero(i) {
    if (i < 10) {
        i = "0" + i;
    }
    return i;
}