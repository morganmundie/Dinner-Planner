
import axios from 'axios';

function DataURIToBlob(dataURI: string) {
    const splitDataURI = dataURI.split(',')
    const byteString = splitDataURI[0].indexOf('base64') >= 0 ? atob(splitDataURI[1]) : decodeURI(splitDataURI[1])
    const mimeString = splitDataURI[0].split(':')[1].split(';')[0]
    const ia = new Uint8Array(byteString.length)
    for (let i = 0; i < byteString.length; i++)
        ia[i] = byteString.charCodeAt(i)

    return new Blob([ia], { type: mimeString })
}

async function getRecipes(){
    try{
        const response = await axios.get('http://localhost:8000/recipe');
        return response.data;
    }
    catch (error){
        console.log(error);
    }
}


async function addRecipe(recipe){
    try{
        const response = await axios.post('http://localhost:8000/recipe/add', recipe);
        return response.data;
    }
    catch (error){
        console.log(error);
    }
}

async function addImage(image, recipeId){
    let file = DataURIToBlob(image);
    let data = new FormData();
    data.append('image', file );
    data.append('recipeId', recipeId);
    data.append('type', file.type);

    try{
        const response = await axios.post('http://localhost:8000/recipe/add/image', data, {headers: {'Content-Type': 'multipart/form-data'}});
        return response.data;
    }
    catch (error){
        console.log(error);
    }
    
}

export {getRecipes, addRecipe, addImage }