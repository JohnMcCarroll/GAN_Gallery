import torch
import torch.optim as optim
import Generator as G
import Discriminator as D
import pickle
import torchvision.transforms as trans
from PIL import ImageCms

# Create/ load networks
G = G.Generator().cuda()
D = D.Discriminator().cuda()

trans = trans.ToPILImage()

### load in data
with open(r'D:\GAN_Gallery\src\dataset1a.db', 'rb') as file:
    dataset1 = pickle.load(file)

real_data = torch.utils.data.DataLoader(dataset1, 10)

### Set up hyperparameters
epoch = 1
lr = 5e-5
counter = 0

### set up optimizer functions
G_solver = optim.RMSprop(G.parameters(), lr=5e-4)
D_solver = optim.RMSprop(D.parameters(), lr=5e-4)

### Training Loop
for epoch in range(epoch):

    for real_sample in real_data:
        # switch to gpu
        real_sample = real_sample.cuda()

        ### Generate batch of G_sample
        latent_space = torch.utils.data.DataLoader([torch.rand(1, 1, 125).cuda(), torch.rand(1, 1, 125).cuda(), torch.rand(1, 1, 125).cuda(), torch.rand(1, 1, 125).cuda(), torch.rand(1, 1, 125).cuda()], 5)   # maybe want more rand inputs for more G samples
        for input in latent_space:
            G_sample = G(input)     ##POTENTIONAL BUG***

        ### train discriminator more than generator?

        ### forward feed D
        D_real = D(real_sample)
        D_fake = D(G_sample)

        ### Reset gradients
        D_solver.zero_grad()
        G_solver.zero_grad()

        ### calculate loss function
        D_loss = -(torch.mean(D_real) - torch.mean(D_fake))             # implementation of wasserstein metric
        G_loss = -torch.mean(D_fake)

        # D_loss = -torch.mean(D_fake) + torch.mean(D_real - 1)
        # G_loss = -(torch.mean(D_real) - torch.mean(D_fake))

        ### train and clipping discriminator weights
        D_loss.backward(retain_graph=True)               # retain_graph=True  (D backwards call effecting G?...***)
        D_solver.step()

        for p in D.parameters():
            p.data.clamp_(-0.01, 0.01)

        ### train generator
        G_loss.backward()
        G_solver.step()

        ### store generator image
        img = trans(G_sample[0].cpu())
        counter += 1
        path = "D:\\GAN_Gallery\\originals\\" + str(counter) + ".jpg"
        img.save(path)

with open(r'D:\GAN_Gallery\src\D_linear.cnn', 'wb') as file:
    pickle.dump(D, file)

with open(r'D:\GAN_Gallery\src\G_linear.cnn', 'wb') as file:
    pickle.dump(G, file)


### BUGS:
# generator has limited variability (add more layers, maybe linear layer from input to inc randomness)
# generator might be updated during disc backprop
# loss functions prioritize discriminator bridging gap...?
# Gan layers/ padding might contribute to "haze" around edge

### IDEAS:
# could separate out gan update and disc update for each batch?
# bias disc towards real data...
# give gen linear layer from input to increase variability of output & reduce jumps between conv trans layers