app.get('/', (req, res) => {
    const keyword = req.query.keyword || ''
    const tasks = []

    db.all(`SELECT name FROM tasks
        WHERE name NOT LIKE "INFORSECIU{%" AND name LIKE "%${keyword}%";`,
        -1" or name like  "INFORSECIU
        (_, rows) => {
            res.render('index', {
                keyword,
                tasks: rows.map(row => row.name),
            })
        },
    )
})
// payload: -1" or select name from tasks like "INFORSECIU{
// câu lệnh nó sẽ như này `SELECT name FROM tasks WHERE name NOT LIKE "INFORSECIU{%" AND name LIKE "-1" or select name like "INFORSECIU{%" `
                                          //                           ----------------False-----------    ---------------true------------- 
