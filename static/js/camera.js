// Selecionando os elementos do DOM
const cameraContainer = document.getElementById("id_camera");
const uploadContainer = document.getElementById("id_form");
const video = document.getElementById("id_webcam");
const canvas = document.getElementById("id_canvas");
const captureBtn = document.getElementById("id_capturar");
const fileInput = document.getElementById("id_imagem");

// Função para iniciar o fluxo da webcam
const iniciarWebcam = () => {
  navigator.mediaDevices
    .getUserMedia({ video: true })
    .then((stream) => {
      video.srcObject = stream;
      video.play();
    })
    .catch((err) => {
      // Se o acesso à webcam for negado ou não disponível
      alert("Não foi possível encontrar a sua webcam.");
      cameraContainer.style.display = 'none';
    });
};

// Função para capturar a imagem da webcam
const capturarImagem = () => {
  const context = canvas.getContext("2d");

  context.drawImage(video, 0, 0, canvas.width, canvas.height);

  // Converter o conteúdo do canvas para um Blob
  canvas.toBlob((blob) => {
    const date = Date.now();
    const file = new File([blob], `captura_${date}.png`, { type: "image/png" });

    //console.log("Arquivo capturado:", file); // Esse arquivo pode ser enviado para o servidor

    // Criar um objeto DataTransfer para adicionar o arquivo ao input
    const dataTransfer = new DataTransfer();
    dataTransfer.items.add(file);
    fileInput.files = dataTransfer.files;
  }, "image/png");
};

// Iniciar a webcam ao carregar a página
iniciarWebcam();

// Adicionar o evento de clique no botão de captura
captureBtn.addEventListener("click", capturarImagem);
