const express = require('express');
const router = express.Router()

const CountryModel = require('../models/Country')

router.get('/', async (request, response) => {
    const countries = await CountryModel.find();
    response.status(200).json(countries);
});

router.get('/names', async (request, response) => {
    const { word } = request.body;
    const result = await CountryModel.find({name : { '$regex' : word, '$options' : 'i' }});
    response.status(200).json(result);
});

router.get('/:id', async (request, response) => {
    try{
    const countryId = request.params.id;

    const countries = await CountryModel.findOne({
        _id: countryId
    });
    
    response.status(200).json(countries);
    }
    catch{
        response.status(500).json("Country not found");
    }
});

router.post('/', async (request, response) => {
    try{
        const {name, isoCode} = request.body
        const country = await CountryModel.create({
            name: name,
            isoCode: isoCode
        });
        response.status(200).json(country);
    }
    catch{
        response.status(500).json('Country not created');
    }
});

router.delete('/:id', async (request, response) => {
    const countryId = request.params.id;

    await CountryModel.findOneAndDelete({
        _id: countryId
    });

    response.status(200).json({msg: 'Country well deleted !'});
});

router.put('/:id', async (request, response) => {
    const countryId = request.params.id;
    const {name, isoCode} = request.body

    const country = await CountryModel.findOneAndUpdate({
        _id: countryId
    },{
        name,
        isoCode
    },{
        new: true
    });

    response.status(200).json(country);
});

module.exports = router;