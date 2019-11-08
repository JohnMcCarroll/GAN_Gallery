import torch
import src.Generator as G
import src.Discriminator as D

# Create/ load networks
G = G.Generator()
D = D.Discriminator()

### load in data


### set up optimizer functions
# G_solver = optim.RMSprop(G.parameters(), lr=5e-5)
# D_solver = optim.RMSprop(D.parameters(), lr=5e-5)

### Training Loop

    ### Generate bathc of G_sample
    # input = random 125 vector(s)
    # G_sample = G(input)

    ### train discriminator more than generator?

        ### forward feed D
        # D_real = D(sample)
        # D_fake = D(G_sample)

        ### calculate loss function
        # D_loss = -(torch.mean(D_real) - torch.mean(D_fake))
        # G_loss = -torch.mean(D_fake)

        ### train and clipping discriminator weights
        # D_loss.backward()
        # D_solver.step()
        #
        # for p in D.parameters():
        #     p.data.clamp_(-0.01, 0.01)

    ### train generator
    # G_loss.backward()
    # G_solver.step()
