"use client";

import { useEffect, useState } from "react";
import axios from "@/lib/axios";
import { jwtDecode } from "jwt-decode";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";

type Device = {
  id: number;
  name: string;
  owner_id: number;
};

type DecodedToken = {
  sub: string; // user ID as a string
  exp: number;
};

export default function DashboardPage() {
  const [deviceName, setDeviceName] = useState("");
  const [devices, setDevices] = useState<Device[]>([]);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      window.location.href = "/auth/login";
    } else {
      fetchDevices(token);
    }
  }, []);

  const fetchDevices = async (token: string) => {
    try {
      const res = await axios.get("/devices", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setDevices(res.data);
    } catch (err) {
      console.error("Failed to fetch devices:", err);
    }
  };

  const handleCreateDevice = async () => {
    const token = localStorage.getItem("token");
    if (!token) return;

    setError("");
    setSuccess("");

    try {
      const decoded = jwtDecode<DecodedToken>(token);
      const owner_id = parseInt(decoded.sub);

      const res = await axios.post(
        "/devices/",
        {
          name: deviceName,
          owner_id,
        },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      setSuccess(`Device "${res.data.name}" created!`);
      setDeviceName("");
      fetchDevices(token);
    } catch (err: any) {
      console.error(err);
      setError(err?.response?.data?.detail || "Failed to create device");
    }
  };

  return (
    <div className="max-w-2xl mx-auto py-16">
      <h1 className="text-3xl font-bold mb-6">Your Devices</h1>

      <div className="mb-8">
        <Label>New Device Name</Label>
        <Input
          value={deviceName}
          onChange={(e) => setDeviceName(e.target.value)}
          placeholder="e.g. Greenhouse Sensor"
          className="mb-2"
        />
        <Button onClick={handleCreateDevice}>Add Device</Button>
        {error && <p className="text-red-500 mt-2">{error}</p>}
        {success && <p className="text-green-600 mt-2">{success}</p>}
      </div>

      <ul className="space-y-2">
        {devices.map((device) => (
          <li key={device.id} className="border p-4 rounded">
            <strong>{device.name}</strong> (ID: {device.id})
          </li>
        ))}
      </ul>

      <Button
        className="mt-6"
        onClick={() => {
          localStorage.removeItem("token");
          window.location.href = "/auth/login";
        }}
      >
        Log Out
      </Button>
    </div>
  );
}
