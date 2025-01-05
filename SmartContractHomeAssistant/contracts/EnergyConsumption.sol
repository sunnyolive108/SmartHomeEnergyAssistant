//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EnergyConsumption {
    struct Consumption {
        uint timestamp;
        uint value; // Verbrauch in kW
    }

    Consumption[] public consumptions;

    function addConsumption(uint _timestamp, uint _value) public {
        consumptions.push(Consumption(_timestamp, _value));
    }

    function getConsumptionCount() public view returns (uint) {
        return consumptions.length;
    }

    function getConsumption(uint _index) public view returns (uint, uint) {
        return (consumptions[_index].timestamp, consumptions[_index].value);
    }
}