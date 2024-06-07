// db.js
import mysql from "mysql2";

const pool = mysql.createPool({
    host: 'localhost',
    user: 'yourusername',
    password: 'yourpassword',
    database: 'yourdatabase',
});

pool.getConnection((err, connection) => {
    if (err instanceof Error) {
        console.log('pool.getConnection error:', err);
        return;
    }
});

export default pool.promise();