async function getAllCupcakes(){
    $('.cupcakes').empty()
    promise = axios.get('http://127.0.0.1:5000/api/cupcakes')
    response = await promise;
    console.log(response.data.cupcakes)
    cupcakes = response.data.cupcakes
    for(let cupcake of cupcakes){
        div = document.createElement('div')
        div.classList.add('cupcake')
        for(let property in cupcake){
            li = document.createElement('li');
            li.textContent = `${property}: ${cupcake[property]}`
            div.append(li)
        }
        document.querySelector('.cupcakes').append(div);
       /*  document.querySelector('body').append(cupcake.flavor) */
        console.log(cupcake.flavor)
    }
    return response.data
}

let cupcakePage = getAllCupcakes();
$('#addBtn').on('click', addCupCake)

async function addCupCake(){
    promise = axios({
        method: 'post',
        url: 'http://127.0.0.1:5000/api/cupcakes',
        data: {
          flavor: document.getElementById('flavor').value,
          size: document.getElementById('size').value,
          rating: document.getElementById('rating').value,
          image: document.getElementById('image').value
        }
      });
      getAllCupcakes()
      return promise
}



