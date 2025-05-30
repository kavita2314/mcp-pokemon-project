const BASE_URL = 'http://localhost:5000/api';

async function getInfo() {
  const name = document.getElementById('infoName').value;
  const res = await fetch(`${BASE_URL}/info`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name })
  });
  const data = await res.json();
  displayInfo(data);
}

async function comparePokemon() {
  const name1 = document.getElementById('compare1').value;
  const name2 = document.getElementById('compare2').value;
  const res = await fetch(`${BASE_URL}/compare`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name1, name2 })
  });
  const data = await res.json();
  displayCompare(data);
}

async function recommendStrategy() {
  const name1 = document.getElementById('strategy1').value;
  const name2 = document.getElementById('strategy2').value;
  const res = await fetch(`${BASE_URL}/strategy`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name1, name2 })
  });
  const data = await res.json();
  displayStrategy(data);
}

async function analyzeTeam() {
  const teamList = document.getElementById('teamList').value.split(',').map(name => name.trim());
  const res = await fetch(`${BASE_URL}/team`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ team: teamList })
  });
  const data = await res.json();
  displayTeam(data);
}

// Display functions for clean output

function displayInfo(data) {
  const output = document.getElementById('infoResult');
  output.innerHTML = `
    <h4>${capitalize(data.name)}</h4>
    <p><strong>Type:</strong> ${data.types.join(', ')}</p>
    <p><strong>Abilities:</strong> ${data.abilities.join(', ')}</p>
    <p><strong>Height:</strong> ${data.height}</p>
    <p><strong>Weight:</strong> ${data.weight}</p>
  `;
}

function displayCompare(data) {
  const output = document.getElementById('compareResult');
  output.innerHTML = `
    <h4>Comparison:</h4>
    <p><strong>${capitalize(data.stronger)}</strong> is stronger.</p>
    <p><strong>Common Types:</strong> ${data.common_types.length ? data.common_types.join(', ') : 'None'}</p>
    <p><strong>Height Difference:</strong> ${data.height_difference}</p>
    <p><strong>Weight Difference:</strong> ${data.weight_difference}</p>
  `;
}

function displayStrategy(data) {
  const output = document.getElementById('strategyResult');
  const poke1 = data.pokemon1.name.toLowerCase();
  const poke2 = data.pokemon2.name.toLowerCase();

  output.innerHTML = `
    <h4>Battle Strategy:</h4>
    <p>${data.strategy}</p>
    <p><strong>Summary:</strong> ${data.summary.join(', ')}</p>
    <p><strong>Type Advantage:</strong></p>
    <ul>
      <li>${capitalize(data.pokemon1.name)}: ${data.type_advantage[poke1]?.map(pair => `${pair[0]} → ${pair[1]}`).join(', ') || 'None'}</li>
      <li>${capitalize(data.pokemon2.name)}: ${data.type_advantage[poke2]?.map(pair => `${pair[0]} → ${pair[1]}`).join(', ') || 'None'}</li>
    </ul>
  `;
}


function displayTeam(data) {
  const output = document.getElementById('teamResult');
  let teamHtml = data.team.map(pokemon => `
    <li><strong>${capitalize(pokemon.name)}</strong> - ${pokemon.types.join(', ')} | 
    Abilities: ${pokemon.abilities.join(', ')} | 
    Stats - Attack: ${pokemon.attack}, Defense: ${pokemon.defense}, Speed: ${pokemon.speed}</li>
  `).join('');

  output.innerHTML = `
    <h4>Team Summary:</h4>
    <p>${data.summary}</p>
    <p><strong>Team Type:</strong> ${data.team_type}</p>
    <p><strong>Total Stats:</strong> 
      Attack = ${data.total_stats.attack}, 
      Defense = ${data.total_stats.defense}, 
      Speed = ${data.total_stats.speed}, 
      Overall = ${data.total_stats.overall}</p>
    <ul>${teamHtml}</ul>
  `;
}

function capitalize(word) {
  return word.charAt(0).toUpperCase() + word.slice(1);
}
