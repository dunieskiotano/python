
import express from 'express';
const express = require("express");
const app = express();

app.use('/', (req, res) => {
  res.status(200).send("This server works");
});
app.listen(3000);
