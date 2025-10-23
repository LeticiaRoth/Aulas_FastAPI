//Definiçao da URL
const API_URL = "http://localhost:8000/api/v1/personagens";

//Função para puxar os dados
async function puxando_api() {
    try {
        const response = await axios.get(API_URL);
        //Conversão em JSON
        return response.data; nte
    } catch (error) {
        console.error("Erro ao buscar personagens:", error);
        return []; 
    }
}

// Mostra os peersonagens no front
async function mostrar_personagens() {
    const personagens = await puxando_api();
    
    const container = document.getElementById("personagens_container");
    container.innerHTML = ""; 

    personagens.forEach(personagem => {
        const personagemDiv = document.createElement('div');
        personagemDiv.classList.add('personagem');

        //Dados da minha model que quero mostrar no meu front
        personagemDiv.innerHTML = `
            <h2>${personagem.nome}</h2>
            <p>Idade: ${personagem.idade}</p>
            <p>Grupo: ${personagem.grupo}</p>
            <hr>
        `;

        container.appendChild(personagemDiv);
    });
}

// Chama a função principal para iniciar
mostrar_personagens();