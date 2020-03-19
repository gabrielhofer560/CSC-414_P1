### Some Kernels:
indentity = np.array([
    [0,0,0],
    [0,1,0],
    [0,0,0]])

blur = np.array([
    [1/9,1/9,1/9],
    [1/9,1/9,1/9],
    [1/9,1/9,1/9]
    ])

sharpen = np.array([
  [0,-1,0],
  [-1,5,-1],
  [0,-1,0]
  ])

emboss = np.array([
  [-2,-1,0],
  [-1,1,1],
  [0,1,2]
  ])

left_sobel = np.array([
  [1,0,-1],
  [2,0,-2],
  [1,0,-1]
  ])

outline = np.array([
  [-1,-1,-1],
  [-1,8,-1],
  [-1,-1,-1]
  ])

