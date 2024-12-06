# informe de Gráficos de Rendimiento y Eficiencia (todo esto es experimental a lo que hay que decir, edita esto luis)
1. Speedup vs. Número de Hilos (CPU)
Descripción: El gráfico muestra cómo mejora el rendimiento (speedup) al incrementar el número de hilos en la CPU. Se incluyen resultados para configuraciones de 4 y 8 hilos comparados con 1 hilo (baseline).

Observaciones:

El speedup aumenta con el número de hilos.
Para 4 hilos, el speedup es más eficiente para tamaños menores del problema, pero empieza a disminuir con problemas mayores.
Para 8 hilos, se observa una mejora adicional, pero no es lineal, indicando limitaciones por overhead y sincronización.
2. Eficiencia Paralela vs. Número de Hilos (CPU)
Descripción: La eficiencia paralela mide qué tan efectivamente se utilizan los recursos disponibles. Se calcula como el speedup dividido por el número de hilos.

Observaciones:

Para 4 hilos, la eficiencia se mantiene alta para tamaños pequeños, pero disminuye para problemas mayores.
Para 8 hilos, la eficiencia es menor en comparación con 4 hilos, lo cual es típico en sistemas donde la sobrecarga crece con el paralelismo.
Conclusión: Un número mayor de hilos no garantiza una eficiencia óptima debido al costo de coordinación y limitaciones del hardware.

3. Speedup vs. Número de Bloques (GPU)
Descripción: Este gráfico muestra el speedup al utilizar 8 bloques comparado con 1 bloque en la GPU.

Observaciones:

El speedup es significativo, lo que demuestra la ventaja de aumentar los bloques en problemas paralelizables.
Sin embargo, los valores tienden a estabilizarse para tamaños grandes, indicando un límite práctico en la mejora que los bloques adicionales pueden proporcionar.
Conclusión: El paralelismo en GPU mejora significativamente el rendimiento, pero el beneficio adicional disminuye a medida que se escala el problema.

4. Eficiencia Paralela vs. Número de Bloques (GPU)
Descripción: La eficiencia paralela en la GPU mide qué tan bien se utilizan los recursos al incrementar el número de bloques.

Observaciones:

La eficiencia se reduce al aumentar los bloques debido a la sobrecarga y la posible falta de trabajo suficiente para llenar todos los bloques.
En problemas grandes, la eficiencia mejora ligeramente debido a una mejor distribución del trabajo.
Conclusión: La GPU aprovecha mejor los bloques adicionales para problemas grandes, pero la eficiencia se ve afectada por la sobrecarga en problemas pequeños.

Conclusiones Generales
CPU:

El speedup mejora con más hilos, pero la eficiencia disminuye debido al overhead.
Es crucial equilibrar el número de hilos con el tamaño del problema para optimizar la eficiencia.
GPU:

Incrementar los bloques mejora significativamente el speedup.
La eficiencia disminuye con bloques adicionales, pero la GPU se desempeña mejor con problemas grandes.
Recomendaciones:

Para CPU: Usar configuraciones de 4 hilos para problemas pequeños y 8 hilos para problemas más grandes.
Para GPU: Incrementar los bloques según el tamaño del problema, pero evitar configuraciones excesivas en problemas pequeños.
Notas Finales:
Los gráficos y los resultados demuestran la importancia de adaptar los parámetros de paralelismo a la naturaleza del problema y
 las características del hardware. Ambos enfoques, CPU y GPU, tienen sus fortalezas y limitaciones, lo que destaca la necesidad de un diseño híbrido en escenarios complejos.