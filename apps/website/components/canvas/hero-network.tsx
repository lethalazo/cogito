"use client"

import { useEffect, useRef } from "react"

interface GraphNode {
  x: number
  y: number
  vx: number
  vy: number
  radius: number
  type: "concept" | "entity" | "connection"
  opacity: number
  phase: number
  pulseIntensity: number
}

interface GraphEdge {
  from: number
  to: number
  weight: number
  targetWeight: number
  flowOffset: number
}

interface Agent {
  x: number
  y: number
  edge: number
  progress: number
  speed: number
  forward: boolean
  trail: { x: number; y: number }[]
}

interface Ripple {
  x: number
  y: number
  radius: number
  opacity: number
}

const CORAL = { r: 212, g: 99, b: 94 }
const BRIGHT = { r: 245, g: 160, b: 155 }
const TRAIL_LEN = 25
const MOUSE_RADIUS = 180

export function HeroNetwork() {
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const stateRef = useRef<{
    nodes: GraphNode[]
    edges: GraphEdge[]
    agents: Agent[]
    ripples: Ripple[]
    adj: Map<number, number[]>
    mouse: { x: number; y: number }
    w: number
    h: number
    time: number
    raf: number
  }>({
    nodes: [],
    edges: [],
    agents: [],
    ripples: [],
    adj: new Map(),
    mouse: { x: -9999, y: -9999 },
    w: 0,
    h: 0,
    time: 0,
    raf: 0,
  })

  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return
    const ctx = canvas.getContext("2d")
    if (!ctx) return
    const s = stateRef.current

    function resize() {
      const dpr = Math.min(window.devicePixelRatio || 1, 2)
      const rect = canvas!.parentElement!.getBoundingClientRect()
      s.w = rect.width
      s.h = rect.height
      canvas!.width = s.w * dpr
      canvas!.height = s.h * dpr
      canvas!.style.width = `${s.w}px`
      canvas!.style.height = `${s.h}px`
      ctx!.setTransform(dpr, 0, 0, dpr, 0, 0)
    }

    function initGraph() {
      const area = s.w * s.h
      const totalNodes = Math.max(20, Math.min(55, Math.floor(area / 18000)))
      const conceptCount = Math.max(4, Math.floor(totalNodes * 0.15))
      const entityCount = Math.floor(totalNodes * 0.35)
      const connectionCount = totalNodes - conceptCount - entityCount
      const agentCount = Math.max(3, Math.min(6, Math.floor(totalNodes / 10)))
      const connectionRange = Math.min(250, Math.max(140, s.w / 5))
      const margin = 50

      // --- Nodes ---
      s.nodes = []

      // Concept nodes: spread in a loose grid for structure
      const cols = Math.max(2, Math.ceil(Math.sqrt(conceptCount * (s.w / s.h))))
      const rows = Math.max(1, Math.ceil(conceptCount / cols))
      for (let i = 0; i < conceptCount; i++) {
        const col = i % cols
        const row = Math.floor(i / cols)
        const cellW = (s.w - margin * 2) / cols
        const cellH = (s.h - margin * 2) / rows
        s.nodes.push({
          x: margin + cellW * (col + 0.2 + Math.random() * 0.6),
          y: margin + cellH * (row + 0.2 + Math.random() * 0.6),
          vx: 0,
          vy: 0,
          radius: 3.5 + Math.random() * 2,
          type: "concept",
          opacity: 0.55 + Math.random() * 0.15,
          phase: Math.random() * Math.PI * 2,
          pulseIntensity: 0,
        })
      }

      // Entity nodes: clustered near concept nodes
      for (let i = 0; i < entityCount; i++) {
        const parent = s.nodes[Math.floor(Math.random() * conceptCount)]
        const angle = Math.random() * Math.PI * 2
        const dist = 40 + Math.random() * 90
        s.nodes.push({
          x: Math.max(margin, Math.min(s.w - margin, parent.x + Math.cos(angle) * dist)),
          y: Math.max(margin, Math.min(s.h - margin, parent.y + Math.sin(angle) * dist)),
          vx: 0,
          vy: 0,
          radius: 2 + Math.random() * 1.5,
          type: "entity",
          opacity: 0.35 + Math.random() * 0.15,
          phase: Math.random() * Math.PI * 2,
          pulseIntensity: 0,
        })
      }

      // Connection nodes: fill the space
      for (let i = 0; i < connectionCount; i++) {
        s.nodes.push({
          x: margin + Math.random() * (s.w - margin * 2),
          y: margin + Math.random() * (s.h - margin * 2),
          vx: 0,
          vy: 0,
          radius: 0.8 + Math.random() * 1,
          type: "connection",
          opacity: 0.2 + Math.random() * 0.15,
          phase: Math.random() * Math.PI * 2,
          pulseIntensity: 0,
        })
      }

      // --- Edges ---
      s.edges = []
      for (let i = 0; i < s.nodes.length; i++) {
        for (let j = i + 1; j < s.nodes.length; j++) {
          const a = s.nodes[i],
            b = s.nodes[j]
          const dx = a.x - b.x,
            dy = a.y - b.y
          const dist = Math.sqrt(dx * dx + dy * dy)
          if (dist > connectionRange) continue

          let prob = 0.08
          if (a.type === "concept" && b.type === "concept") prob = 0.6
          else if (a.type === "concept" || b.type === "concept") prob = 0.25
          else if (a.type === "entity" && b.type === "entity") prob = 0.12

          if (Math.random() < prob) {
            const w = 0.2 + Math.random() * 0.8
            s.edges.push({
              from: i,
              to: j,
              weight: w,
              targetWeight: w,
              flowOffset: Math.random() * 100,
            })
          }
        }
      }

      // Ensure every node has at least one edge
      for (let i = 0; i < s.nodes.length; i++) {
        const hasEdge = s.edges.some((e) => e.from === i || e.to === i)
        if (!hasEdge) {
          let nearest = 0,
            nearestDist = Infinity
          for (let j = 0; j < s.nodes.length; j++) {
            if (i === j) continue
            const dx = s.nodes[i].x - s.nodes[j].x
            const dy = s.nodes[i].y - s.nodes[j].y
            const d = dx * dx + dy * dy
            if (d < nearestDist) {
              nearestDist = d
              nearest = j
            }
          }
          s.edges.push({
            from: Math.min(i, nearest),
            to: Math.max(i, nearest),
            weight: 0.3 + Math.random() * 0.4,
            targetWeight: 0.3 + Math.random() * 0.4,
            flowOffset: Math.random() * 100,
          })
        }
      }

      // Build adjacency map
      s.adj = new Map()
      for (let i = 0; i < s.nodes.length; i++) s.adj.set(i, [])
      for (let ei = 0; ei < s.edges.length; ei++) {
        s.adj.get(s.edges[ei].from)!.push(ei)
        s.adj.get(s.edges[ei].to)!.push(ei)
      }

      // --- Agents ---
      s.agents = []
      for (let i = 0; i < agentCount; i++) {
        const ei = Math.floor(Math.random() * s.edges.length)
        const edge = s.edges[ei]
        s.agents.push({
          x: s.nodes[edge.from].x,
          y: s.nodes[edge.from].y,
          edge: ei,
          progress: 0,
          speed: 0.004 + Math.random() * 0.004,
          forward: true,
          trail: [],
        })
      }

      s.ripples = []
    }

    function draw() {
      s.time += 0.016
      ctx!.clearRect(0, 0, s.w, s.h)
      const { nodes, edges, agents, ripples, adj, mouse, time } = s

      // --- Node physics: repulsion ---
      for (let i = 0; i < nodes.length; i++) {
        for (let j = i + 1; j < nodes.length; j++) {
          const a = nodes[i],
            b = nodes[j]
          const dx = a.x - b.x,
            dy = a.y - b.y
          const distSq = dx * dx + dy * dy
          if (distSq < 2500 && distSq > 0) {
            const dist = Math.sqrt(distSq)
            const f = ((50 - dist) / 50) * 0.02
            const fx = (dx / dist) * f,
              fy = (dy / dist) * f
            a.vx += fx
            a.vy += fy
            b.vx -= fx
            b.vy -= fy
          }
        }
      }

      // Apply damping + tiny wander + boundaries
      for (const n of nodes) {
        n.vx += (Math.random() - 0.5) * 0.008
        n.vy += (Math.random() - 0.5) * 0.008
        n.vx *= 0.96
        n.vy *= 0.96
        n.x += n.vx
        n.y += n.vy
        if (n.x < 20) n.vx += 0.03
        if (n.x > s.w - 20) n.vx -= 0.03
        if (n.y < 20) n.vy += 0.03
        if (n.y > s.h - 20) n.vy -= 0.03
        n.pulseIntensity *= 0.96
      }

      // --- Agents: traverse edges ---
      for (const agent of agents) {
        const edge = edges[agent.edge]
        if (!edge) continue
        const fromIdx = agent.forward ? edge.from : edge.to
        const toIdx = agent.forward ? edge.to : edge.from
        const fn = nodes[fromIdx],
          tn = nodes[toIdx]

        agent.progress += agent.speed
        agent.x = fn.x + (tn.x - fn.x) * agent.progress
        agent.y = fn.y + (tn.y - fn.y) * agent.progress

        agent.trail.push({ x: agent.x, y: agent.y })
        if (agent.trail.length > TRAIL_LEN) agent.trail.shift()

        // Reached destination node
        if (agent.progress >= 1) {
          nodes[toIdx].pulseIntensity = 1
          ripples.push({ x: tn.x, y: tn.y, radius: tn.radius, opacity: 0.25 })

          const adjEdges = adj.get(toIdx)
          if (adjEdges && adjEdges.length > 0) {
            const opts = adjEdges.filter((ei) => ei !== agent.edge)
            const next =
              opts.length > 0
                ? opts[Math.floor(Math.random() * opts.length)]
                : adjEdges[Math.floor(Math.random() * adjEdges.length)]
            agent.edge = next
            agent.forward = edges[next].from === toIdx
            agent.progress = 0
          }
        }
      }

      // --- Ripples: expand and fade ---
      for (let i = ripples.length - 1; i >= 0; i--) {
        ripples[i].radius += 1.2
        ripples[i].opacity -= 0.008
        if (ripples[i].opacity <= 0) ripples.splice(i, 1)
      }

      // --- Evolve: slowly shift edge weights ---
      if (Math.random() < 0.008) {
        const idx = Math.floor(Math.random() * edges.length)
        edges[idx].targetWeight = 0.15 + Math.random() * 0.85
      }
      for (const e of edges) {
        e.weight += (e.targetWeight - e.weight) * 0.008
      }

      // --- Mouse: highlight local subgraph ---
      let highlightNode = -1
      if (mouse.x > -999) {
        let closest = MOUSE_RADIUS
        for (let i = 0; i < nodes.length; i++) {
          const dx = nodes[i].x - mouse.x,
            dy = nodes[i].y - mouse.y
          const d = Math.sqrt(dx * dx + dy * dy)
          if (d < closest) {
            closest = d
            highlightNode = i
          }
        }
      }
      const hlEdges = new Set<number>()
      const hlNodes = new Set<number>()
      if (highlightNode >= 0) {
        hlNodes.add(highlightNode)
        for (const ei of adj.get(highlightNode) || []) {
          hlEdges.add(ei)
          hlNodes.add(edges[ei].from)
          hlNodes.add(edges[ei].to)
        }
      }

      // --- Draw edges ---
      ctx!.setLineDash([3, 5])
      for (let ei = 0; ei < edges.length; ei++) {
        const e = edges[ei]
        const a = nodes[e.from],
          b = nodes[e.to]
        const isHl = hlEdges.has(ei)
        const alpha = isHl ? Math.min(e.weight * 0.45, 0.5) : e.weight * 0.12
        const lw = isHl ? e.weight * 1.8 + 0.3 : e.weight * 0.7 + 0.2

        ctx!.lineDashOffset = -time * 12 + e.flowOffset
        ctx!.lineWidth = lw
        ctx!.strokeStyle = `rgba(${CORAL.r},${CORAL.g},${CORAL.b},${alpha})`
        ctx!.beginPath()
        ctx!.moveTo(a.x, a.y)
        ctx!.lineTo(b.x, b.y)
        ctx!.stroke()
      }
      ctx!.setLineDash([])

      // --- Draw ripples ---
      for (const r of ripples) {
        ctx!.beginPath()
        ctx!.arc(r.x, r.y, r.radius, 0, Math.PI * 2)
        ctx!.strokeStyle = `rgba(${CORAL.r},${CORAL.g},${CORAL.b},${r.opacity})`
        ctx!.lineWidth = 0.8
        ctx!.stroke()
      }

      // --- Draw nodes ---
      for (let i = 0; i < nodes.length; i++) {
        const n = nodes[i]
        const pulse = Math.sin(time * 1.2 + n.phase) * 0.12 + 0.88
        const isHl = hlNodes.has(i)
        let alpha = n.opacity * pulse + n.pulseIntensity * 0.4
        if (isHl) alpha = Math.min(alpha + 0.25, 1)

        // Glow
        const gr = n.radius * (3.5 + n.pulseIntensity * 4)
        const g = ctx!.createRadialGradient(n.x, n.y, 0, n.x, n.y, gr)
        g.addColorStop(
          0,
          `rgba(${CORAL.r},${CORAL.g},${CORAL.b},${alpha * 0.2})`
        )
        g.addColorStop(1, `rgba(${CORAL.r},${CORAL.g},${CORAL.b},0)`)
        ctx!.beginPath()
        ctx!.arc(n.x, n.y, gr, 0, Math.PI * 2)
        ctx!.fillStyle = g
        ctx!.fill()

        // Core
        ctx!.beginPath()
        ctx!.arc(
          n.x,
          n.y,
          n.radius * (1 + n.pulseIntensity * 0.3),
          0,
          Math.PI * 2
        )
        ctx!.fillStyle = `rgba(${CORAL.r},${CORAL.g},${CORAL.b},${alpha})`
        ctx!.fill()

        // Concept nodes: bright center + subtle ring
        if (n.type === "concept") {
          ctx!.beginPath()
          ctx!.arc(n.x, n.y, n.radius * 0.35, 0, Math.PI * 2)
          ctx!.fillStyle = `rgba(255,255,255,${alpha * 0.35})`
          ctx!.fill()
          ctx!.beginPath()
          ctx!.arc(n.x, n.y, n.radius * 2.2, 0, Math.PI * 2)
          ctx!.strokeStyle = `rgba(${CORAL.r},${CORAL.g},${CORAL.b},${alpha * 0.12})`
          ctx!.lineWidth = 0.5
          ctx!.stroke()
        }
      }

      // --- Draw agents ---
      for (const agent of agents) {
        // Trail: fading line
        for (let i = 1; i < agent.trail.length; i++) {
          const prev = agent.trail[i - 1],
            curr = agent.trail[i]
          const t = i / agent.trail.length
          ctx!.beginPath()
          ctx!.moveTo(prev.x, prev.y)
          ctx!.lineTo(curr.x, curr.y)
          ctx!.strokeStyle = `rgba(${BRIGHT.r},${BRIGHT.g},${BRIGHT.b},${t * 0.3})`
          ctx!.lineWidth = t * 1.8
          ctx!.stroke()
        }

        // Body
        ctx!.beginPath()
        ctx!.arc(agent.x, agent.y, 2.5, 0, Math.PI * 2)
        ctx!.fillStyle = `rgba(${BRIGHT.r},${BRIGHT.g},${BRIGHT.b},0.9)`
        ctx!.fill()

        // Glow
        const ag = ctx!.createRadialGradient(
          agent.x,
          agent.y,
          0,
          agent.x,
          agent.y,
          14
        )
        ag.addColorStop(
          0,
          `rgba(${BRIGHT.r},${BRIGHT.g},${BRIGHT.b},0.18)`
        )
        ag.addColorStop(1, `rgba(${BRIGHT.r},${BRIGHT.g},${BRIGHT.b},0)`)
        ctx!.beginPath()
        ctx!.arc(agent.x, agent.y, 14, 0, Math.PI * 2)
        ctx!.fillStyle = ag
        ctx!.fill()
      }

      s.raf = requestAnimationFrame(draw)
    }

    const onMove = (e: MouseEvent) => {
      const r = canvas!.getBoundingClientRect()
      s.mouse.x = e.clientX - r.left
      s.mouse.y = e.clientY - r.top
    }
    const onLeave = () => {
      s.mouse.x = -9999
      s.mouse.y = -9999
    }

    let resizeTimer: ReturnType<typeof setTimeout>
    const handleResize = () => {
      clearTimeout(resizeTimer)
      resizeTimer = setTimeout(() => {
        resize()
        initGraph()
      }, 150)
    }

    resize()
    initGraph()
    s.raf = requestAnimationFrame(draw)
    window.addEventListener("resize", handleResize)
    canvas.addEventListener("mousemove", onMove)
    canvas.addEventListener("mouseleave", onLeave)

    return () => {
      cancelAnimationFrame(s.raf)
      clearTimeout(resizeTimer)
      window.removeEventListener("resize", handleResize)
      canvas.removeEventListener("mousemove", onMove)
      canvas.removeEventListener("mouseleave", onLeave)
    }
  }, [])

  return (
    <canvas
      ref={canvasRef}
      aria-hidden="true"
      role="presentation"
      className="absolute inset-0 w-full h-full"
      style={{ display: "block" }}
    />
  )
}
