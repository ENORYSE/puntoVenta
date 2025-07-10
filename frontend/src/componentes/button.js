function Button(){
    const button = document.createElement('button');
    button.className = "text-xl bg-[#333] rounded-2xl px-5 py-2";
    button.innerHTML = 'Hola';
    return button;
}

export default Button;