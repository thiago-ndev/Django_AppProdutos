const form = document.getElementById('login-form');

form.addEventListener('submit', function(event) {
  event.preventDefault();

  const email = document.getElementById('email').value;
  const senha = document.getElementById('senha').value;

  if (email === '') {
    alert('Por favor, digite seu e-mail.');
    return;
  }

  if (senha === '') {
    alert('Por favor, digite sua senha.');
    return;
  }

  alert('Login efetuado com sucesso!');
  // aqui você pode enviar o formulário ou redirecionar o usuário para outra página
});