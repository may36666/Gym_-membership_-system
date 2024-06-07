// server.js
import express from "express";
import bodyParser from "body-parser";
import db from "./config/db.mjs";

const app = express();
app.use(bodyParser.json());

const PORT = process.env.PORT || 3000;

// Test database connection
app.get('/test', async (req, res) => {
    try {
        const [rows] = await db.query('SELECT 1 + 1 AS result');
        res.json(rows[0]);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// Create a new record
app.post('/api/records', async (req, res) => {
    const { name, age } = req.body;
    try {
        const [result] = await db.query('INSERT INTO records (name, age) VALUES (?, ?)', [name, age]);
        res.status(201).json({ id: result.insertId, name, age });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// Get all records
app.get('/api/records', async (req, res) => {
    try {
        const [rows] = await db.query('SELECT * FROM records');
        res.json(rows);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// Get a specific record
app.get('/api/records/:id', async (req, res) => {
    const { id } = req.params;
    try {
        const [rows] = await db.query('SELECT * FROM records WHERE id = ?', [id]);
        if (rows.length === 0) {
            return res.status(404).json({ error: 'Record not found' });
        }
        res.json(rows[0]);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// Update a record
app.put('/api/records/:id', async (req, res) => {
    const { id } = req.params;
    const { name, age } = req.body;
    try {
        const [result] = await db.query('UPDATE records SET name = ?, age = ? WHERE id = ?', [name, age, id]);
        if (result.affectedRows === 0) {
            return res.status(404).json({ error: 'Record not found' });
        }
        res.json({ id, name, age });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// Delete a record
app.delete('/api/records/:id', async (req, res) => {
    const { id } = req.params;
    try {
        const [result] = await db.query('DELETE FROM records WHERE id = ?', [id]);
        if (result.affectedRows === 0) {
            return res.status(404).json({ error: 'Record not found' });
        }
        res.status(204).send();
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});