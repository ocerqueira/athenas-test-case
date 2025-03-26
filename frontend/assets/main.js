// URL da API com versão v1 incluída
const API_URL = 'http://localhost:8000/api/v1/pessoas/';
let pessoas = [];
let editId = null;

// Helper para obter elementos pelo ID
const $ = id => document.getElementById(id);

// Carrega as pessoas da API 
const carregarPessoas = () => {
  axios.get(API_URL)
    .then(({ data }) => {
      pessoas = data;
      renderTable();
    })
    .catch(() => alert('Erro ao carregar pessoas.'));
};

const capitalizeName = name => {
  return name
    .split(' ')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
    .join(' ');
};

// Função para formatar o CPF (ex: 12345678901 → 123.456.789-01)
const formatCPF = cpf => {
  cpf = cpf.replace(/\D/g, '');
  if (cpf.length === 11) {
    return cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4');
  }
  return cpf;
};

// Renderiza a tabela com os dados das pessoas
const renderTable = () => {
  const tableBody = $('peopleTable');
  tableBody.innerHTML = '';
  pessoas.forEach(pessoa => {
    const tr = document.createElement('tr');
    tr.className = 'border-b hover:bg-gray-100';
    tr.innerHTML = `
      <td class="py-3 px-6 text-left">${pessoa.id}</td>
      <td class="py-3 px-6 text-left">${capitalizeName(pessoa.nome)}</td>
      <td class="py-3 px-6 text-left">${formatCPF(pessoa.cpf)}</td>
      <td class="py-3 px-6 text-left">${pessoa.altura}</td>
      <td class="py-3 px-6 text-left">${pessoa.peso}</td>
      <td class="py-3 px-6 text-left">${pessoa.sexo === 'M' ? 'Masculino' : 'Feminino'}</td>
      <td class="py-3 px-6 text-center space-x-2">
        <button onclick="editarPessoa(${pessoa.id})" class="bg-yellow-500 hover:bg-yellow-600 text-white py-1 px-3 rounded">Editar</button>
        <button onclick="excluirPessoa(${pessoa.id})" class="bg-red-500 hover:bg-red-600 text-white py-1 px-3 rounded">Excluir</button>
        <button onclick="pesoIdeal(${pessoa.id})" class="bg-green-500 hover:bg-green-600 text-white py-1 px-3 rounded">Peso Ideal</button>
      </td>
    `;
    tableBody.appendChild(tr);
  });
};

// Fecha o popover/modal
const fecharPopover = () => {
  const popoverEl = $('formContainer');
  if (popoverEl.popover && typeof popoverEl.popover.close === 'function') {
    popoverEl.popover.close();
  } else {
    popoverEl.style.display = 'none';
  }
};

// Manipula o envio do formulário para salvar ou editar pessoa
const handleFormSubmit = e => {
  e.preventDefault();
  const dados = {
    nome: $('nome').value,
    cpf: $('cpf').value,
    data_nasc: $('data_nasc').value,
    altura: parseInt($('altura').value),
    peso: parseFloat($('peso').value),
    sexo: $('sexo').value
  };

  const request = editId 
    ? axios.put(`${API_URL}${editId}/`, dados)
    : axios.post(API_URL, dados);

  request
    .then(() => {
      carregarPessoas();
      fecharPopover();
    })
    .catch(() => alert(editId ? 'Erro ao editar pessoa.' : 'Erro ao adicionar pessoa.'));
};

// Preenche o formulário com os dados da pessoa para edição
const editarPessoa = id => {
  const pessoa = pessoas.find(p => p.id === id);
  if (!pessoa) return;
  editId = id;
  $('nome').value = pessoa.nome;
  $('cpf').value = pessoa.cpf;
  $('data_nasc').value = pessoa.data_nasc;
  $('altura').value = pessoa.altura;
  $('peso').value = pessoa.peso;
  $('sexo').value = pessoa.sexo;
  $('formTitle').textContent = 'Editar Pessoa';
  const popoverEl = $('formContainer');
  if (popoverEl.popover && typeof popoverEl.popover.show === 'function') {
    popoverEl.popover.show();
  } else {
    popoverEl.style.display = 'block';
  }
};

// Exclui a pessoa via API com confirmação
const excluirPessoa = id => {
  Swal.fire({
    title: 'Tem certeza?',
    text: "Você não poderá reverter esta ação!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Sim, excluir!'
  }).then(result => {
    if (result.isConfirmed) {
      axios.delete(`${API_URL}${id}/`)
        .then(() => {
          carregarPessoas();
          Swal.fire('Excluído!', 'A pessoa foi excluída com sucesso.', 'success');
        })
        .catch(() => {
          Swal.fire('Erro', 'Erro ao excluir pessoa.', 'error');
        });
    }
  });
};

// Busca e exibe o peso ideal
const pesoIdeal = id => {
  axios.get(`${API_URL}${id}/peso-ideal/`)
    .then(({ data }) => {
      Swal.fire({
        title: 'Peso Ideal',
        text: `O peso ideal é ${data.peso_ideal}`,
        icon: 'info',
        confirmButtonText: 'Fechar'
      });
    })
    .catch(() => {
      Swal.fire({
        title: 'Erro',
        text: 'Erro ao calcular o peso ideal.',
        icon: 'error',
        confirmButtonText: 'Fechar'
      });
    });
};

// Abre o formulário para adicionar nova pessoa
const openAddForm = () => {
  editId = null;
  $('personForm').reset();
  $('formTitle').textContent = 'Adicionar Pessoa';
  const popoverEl = $('formContainer');
  if (popoverEl.popover && typeof popoverEl.popover.show === 'function') {
    popoverEl.popover.show();
  } else {
    popoverEl.style.display = 'block';
  }
};

// Botão para atualizar a lista
$('btnRefresh').addEventListener('click', () => {
  carregarPessoas();
});

// Inicializa os eventos (sem campo de busca)
const init = () => {
  $('cancelBtn').addEventListener('click', fecharPopover);
  $('personForm').addEventListener('submit', handleFormSubmit);
  $('btnAdd').addEventListener('click', openAddForm);
};

init();
