import os
import unittest

class TestCognitiveMeshEcosystem(unittest.TestCase):
    
    def test_workspace_modules_existence(self):
        """Valida a presença de todos os módulos essenciais da vanguarda no diretório src/"""
        required_modules = [
            "cognitive_mesh_engine.py",
            "post_quantum_tunnel.py",
            "autonomous_grc_engine.py",
            "jit_meta_orchestrator.py",
            "federated_ai_core.py",
            "self_healing_chaos_engine.py",
            "swarm_resonance_core.py",
            "hyperdimensional_core.py",
            "singularity_core.py",
            "omega_singularity_mesh.py",
            "telemetry_observer_core.py",
            "hyper_matrix_hypervisor.py",
            "quantum_synthetic_governor.py",
            "holographic_singularity_mesh.py",
            "quantum_metamorphic_governor.py"
        ]
        
        for module in required_modules:
            module_path = os.path.join("src", module)
            self.assertTrue(os.path.exists(module_path), f"Módulo crítico ausente: {module}")

    def test_shared_memory_permissions(self):
        """Valida se o ambiente suporta a criação de estruturas em /dev/shm"""
        shm_test_path = "/dev/shm/ecosystem_integrity_check"
        try:
            with open(shm_test_path, "wb") as f:
                f.write(b'\x00' * 1024)
            self.assertTrue(os.path.exists(shm_test_path))
        finally:
            if os.path.exists(shm_test_path):
                os.remove(shm_test_path)

if __name__ == "__main__":
    unittest.main()
