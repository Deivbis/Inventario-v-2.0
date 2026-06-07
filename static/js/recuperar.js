function togglePassword(id) {
  const input = document.getElementById(id);
  input.type = input.type === 'password' ? 'text' : 'password';
}

document.getElementById('recuperarForm').addEventListener('submit', function (event) {
  const nueva = document.getElementById('nueva').value;
  const confirmar = document.getElementById('confirmar').value;
  const error = document.getElementById('error-msg');

  if (nueva !== confirmar) {
    event.preventDefault();
    error.style.display = 'block';
  } else {
    error.style.display = 'none';
  }
});
