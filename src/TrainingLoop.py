import torch
import torch.optim as optim
import src.Generator as G
import src.Discriminator as D
import pickle
import torchvision.transforms as trans
import gc

# Create/ load networks
G = G.Generator().cuda()
D = D.Discriminator().cuda()

# with open(r'D:\GAN_Gallery\src\D_linear.cnn', 'rb') as file:
#     D = pickle.load(file)

# with open(r'D:\GAN_Gallery\src\G_linear.cnn', 'rb') as file:
#     G = pickle.load(file)

trans = trans.ToPILImage()

### Set up hyperparameters
epochs = 5
lr = 5e-5
counter = 0

### Training Loop
for epoch in range(epochs * 3):

    ### cycle in in data
    dataset = []
    real_data = []
    gc.collect()

    if epoch % 3 == 0:
        with open(r'D:\GAN_Gallery\src\dataset1a.db', 'rb') as file:
            dataset = pickle.load(file)
    elif epoch % 3 == 1:
        with open(r'D:\GAN_Gallery\src\dataset2a.db', 'rb') as file:
            dataset = pickle.load(file)
    else:
        with open(r'D:\GAN_Gallery\src\dataset3a.db', 'rb') as file:
            dataset = pickle.load(file)

    real_data = torch.utils.data.DataLoader(dataset, 10, True)

    ### set up optimizer functions
    G_solver = optim.RMSprop(G.parameters(), lr=5e-5)
    D_solver = optim.RMSprop(D.parameters(), lr=5e-5)
    D_grounder = optim.Adam(D.parameters(), lr=2e-5)

    MSELoss = torch.nn.MSELoss()

    ### training
    iterations = 0
    for real_sample in real_data:

        # switch to gpu
        real_sample = real_sample.cuda()

        # Generate batch of G_sample
        latent_space = torch.utils.data.DataLoader(
            [torch.rand(1, 1, 125).cuda(), torch.rand(1, 1, 125).cuda(), torch.rand(1, 1, 125).cuda(),
             torch.rand(1, 1, 125).cuda(), torch.rand(1, 1, 125).cuda(), torch.rand(1, 1, 125).cuda(),
             torch.rand(1, 1, 125).cuda(), torch.rand(1, 1, 125).cuda(), torch.rand(1, 1, 125).cuda(),
             torch.rand(1, 1, 125).cuda()], 10)

        for input in latent_space:
            G_sample = G(input).detach()

        ### TRAIN DISCRIMINATOR ###

        # forward feed D
        D_real = D(real_sample)
        D_fake = D(G_sample)

        ##what is the output ******
        print("outputs:")
        print(D_real[0])
        print(D_fake[0])

        # calculate discriminator loss function
        D_loss = -(torch.mean(D_real) - torch.mean(D_fake))     # implementation of wasserstein metric
        print("D loss:")
        print(D_loss.item())

        # train and clipping discriminator weights
        D_loss.backward()
        D_solver.step()

        for p in D.parameters():
            p.data.clamp_(-0.01, 0.01)

        # reset gradients
        D_solver.zero_grad()

        # increment iterations
        iterations += 1

        ### TRAIN GENERATOR PERIODICALLY ###
        if iterations % 5 == 0:
            # Train Generator

            # Generate batch of G_sample
            latent_space = torch.utils.data.DataLoader(
                [torch.rand(1, 1, 125).cuda(), torch.rand(1, 1, 125).cuda(), torch.rand(1, 1, 125).cuda(),
                 torch.rand(1, 1, 125).cuda(), torch.rand(1, 1, 125).cuda(), torch.rand(1, 1, 125).cuda(),
                 torch.rand(1, 1, 125).cuda(), torch.rand(1, 1, 125).cuda(), torch.rand(1, 1, 125).cuda(),
                 torch.rand(1, 1, 125).cuda()], 10)

            for input in latent_space:
                G_output = G(input)

            # calculate generator adervasrial loss
            G_loss = -torch.mean(D(G_output))
            print("G loss:")
            print(G_loss.item())

            # train generator
            G_loss.backward()
            G_solver.step()

            # Reset gradients
            G_solver.zero_grad()

            ### store generator image
            img = trans(G_sample[0].cpu())
            counter += 1
            path = "D:\\GAN_Gallery\\originals\\" + str(counter) + ".jpg"
            img.save(path)

            # GROUND DISCRIMINATOR              EXPERIMENTAL***
            for j in range(0, len(real_sample)):
                prediction = D(real_sample[j].unsqueeze(0))
                target = torch.ones([1,1,1,1]).cuda()
                loss = MSELoss(prediction, target)
                print("D_ground:")
                print(loss)
                loss.backward()
                D_grounder.step()
                D_grounder.zero_grad()


with open(r'discriminator.cnn', 'wb') as file:
    pickle.dump(D, file)

with open(r'generator.cnn', 'wb') as file:
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
