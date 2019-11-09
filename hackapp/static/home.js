//모달 열기
function openModal(x, y, el) {
  console.log("open", x, y, el);
  if(el.querySelectorAll("img").length === 0) document.querySelector("#modal").classList.add("on");
}
//모달 열기
function closeModal() {
  document.querySelector("#modal").classList.remove("on");
}

//토글 뷰
function toggleView(idx) {
  document.querySelector(".view.show").classList.remove("show");
  document.querySelectorAll(".view")[idx].classList.add("show");
}

//
function toggleSub(){
  document.querySelector(".form.sub").classList.add("show");
}

// 맵 환경 작업
function mapDrawing() {
  const w = window.innerWidth;
  const h = window.innerHeight;

  const boxSize = 32;

  const verticalCount = Math.ceil(w / boxSize);
  const horizonCount = Math.ceil(h / boxSize);

  // 기본 타일 배열 생성
  const drawingArray = Array(verticalCount)
    .fill(null)
    .map(() => Array(horizonCount).fill(false));

  // 랜덤한 칸에 잔디 심기 및 해당 칸 주위에 추가 잔디 심기
  let dumpArray = [...drawingArray];
  dumpArray.map((arr, i) => {
    arr.map((bool, j) => {
      if (Math.floor(Math.random() * 10) % 10 === 0) {
        drawingArray[i][j] = true;

        if (i - 1 >= 0) {
          drawingArray[i - 1][j] = true;
        }
        if (i + 1 < arr.length) {
          drawingArray[i + 1][j] = true;
        }
        if (j - 1 >= 0) {
          drawingArray[i][j - 1] = true;

          if (i - 1 >= 0) {
            drawingArray[i - 1][j - 1] = true;
          }
          if (i + 1 < arr.length) {
            drawingArray[i + 1][j - 1] = true;
          }
        }
      }
    });
  });

  // 상하좌우 다 잔디가 심어져 있으나 자기 칸만 잔디가 없을 경우, 잔디 심기
  dumpArray = [...drawingArray];
  dumpArray.map((arr, i) => {
    arr.map((bool, j) => {
      if (
        bool === false &&
        (i - 1 >= 0 && drawingArray[i - 1][j] === true) &&
        (i + 1 < arr.length && drawingArray[i + 1][j] === true) &&
        (j - 1 >= 0 && drawingArray[i][j - 1] === true) &&
        (j + 1 < arr.length && drawingArray[i][j + 1] === true)
      ) {
        drawingArray[i][j] = true;
      }
    });
  });

  // 위에서 열심히 심은 잔디 배열을 화면에 출력
  drawingArray.map((arr, i) => {
    arr.map((bool, j) => {
      const box = document.createElement("div");
      box.addEventListener("click", function () {
        openModal(i, j, this);
      });

      if (bool) {
        box.setAttribute("class", "box on");
      } else {
        box.setAttribute("class", "box");
      }
      box.setAttribute("style", `top: ${32 * j}px; left: ${32 * i}px`);
      document.querySelector(".greenWrap").appendChild(box);
    });
  });
}

document.addEventListener("DOMContentLoaded", event => {
  mapDrawing();
});
