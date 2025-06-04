document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.confetti').forEach(function (btn) {
        btn.addEventListener('click', function () {
            for (let i = 0; i < 20; i++) {
                confetti({
                    particleCount: 100,
                    startVelocity: 30,
                    spread: 360,
                    origin: {
                        x: Math.random(),
                        y: Math.random() - 0.2
                    }
                });
            }
        });
    });
});