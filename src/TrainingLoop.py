import torch
import torch.optim as optim
import src.Generator as G
import src.Discriminator as D
import pickle
import torchvision.transforms as trans
from PIL import Image

# Create/ load networks
G = G.Generator()
D = D.Discriminator()

### load in data
with open(r'D:\GAN_Gallery\src\dataset1.db', 'rb') as file:
    dataset1 = pickle.load(file)

real_data = torch.utils.data.DataLoader(dataset1, 10)

### set up optimizer functions
G_solver = optim.RMSprop(G.parameters(), lr=5e-5)
D_solver = optim.RMSprop(D.parameters(), lr=5e-5)

### Set up hyperparameters
epoch = 1

### Training Loop
for epoch in range(epoch):

    for real_sample in real_data:

        ### Generate bathc of G_sample
        input = [torch.rand(125), torch.rand(125), torch.rand(125), torch.rand(125), torch.rand(125)]    # maybe want more rand inputs for more G samples
        G_sample = G(input)         # cant use list??***

        ### print generator image
        img = trans.ToPILImage(G_sample[0])
        img.show()

        ### train discriminator more than generator?

        ### forward feed D
        D_real = D(real_sample)
        D_fake = D(G_sample)

        ### calculate loss function
        D_loss = -(torch.mean(D_real) - torch.mean(D_fake))             # implementation of wasserstein metric
        G_loss = -torch.mean(D_fake)

        ### train and clipping discriminator weights
        D_loss.backward()
        D_solver.step()

        for p in D.parameters():
            p.data.clamp_(-0.01, 0.01)

        ### train generator
        G_loss.backward()
        G_solver.step()

with open(r'D:\GAN_Gallery\src\D.cnn', 'wb') as file:
    pickle.dump(D, file)

with open(r'D:\GAN_Gallery\src\G.cnn', 'wb') as file:
    pickle.dump(G, file)