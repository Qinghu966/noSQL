const express = require('express');
const router = express.Router()

const ContinentModel = require('../models/Continent')

router.get('/', async (request, response) => {
    const continents = await ContinentModel.find().populate('countries');
    response.status(200).json(continents);
});

router.post('/', async (request, response) => {
        const {name, countries } = request.body
        const result = await ContinentModel.create({
            name: name,
            countries: countries
        });
        response.status(200).json(result);
});

router.get('/withThreeCountries/', async (request, response) => {
        const {name, countries } = request.body
        const countinentsResult = await ContinentModel.find({countries:  {$size: 3}});
       
        response.status(200).json(countinentsResult);
  
});

module.exports = router;