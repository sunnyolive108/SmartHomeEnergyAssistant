// Importiere den Smart Contract, den du deployen möchtest
const EnergyConsumption = artifacts.require("EnergyConsumption");

module.exports = function (deployer) {
  // Deploye den EnergyConsumption Contract
  deployer.deploy(EnergyConsumption);
};
